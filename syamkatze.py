import argparse
from pathlib import Path
from typing import Iterator, Callable

SearchFunction = Callable[[Path], Iterator[Path]]


class Arguments:
    def __init__(self, directory_path: Path, recursive: bool, delete: bool, verbose: bool) -> None:
        self.directory_path: Path = directory_path
        self.recursive: bool = recursive
        self.delete: bool = delete
        self.verbose: bool = verbose


class ArgumentsParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser(
            usage="%(prog)s [OPTION] [DIRECTORY]...",
            description="Siamkatze is a tool to find and manage broken symbolic links.",
            epilog="python siamkatze.py [-h] [-r] [-d] directory_path"
        )
        self.parser.add_argument("directory_path", help="Path to the directory")
        self.parser.add_argument("-r", "--recursive", action="store_true", help="Enable recursive search")
        self.parser.add_argument("-d", "--delete", action="store_true", help="Enable deletion of broken links")
        self.parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode")

    def parse(self) -> Arguments:
        args = self.parser.parse_args()
        return Arguments(args.directory_path, args.recursive, args.delete, args.verbose)


class Configuration:
    def __init__(self, arguments: Arguments) -> None:
        self.arguments: Arguments = arguments

    @property
    def verbose(self) -> bool:
        return self.arguments.verbose

    @property
    def delete_symlinks(self) -> bool:
        return self.arguments.delete

    @property
    def recursive_search(self) -> bool:
        return self.arguments.recursive

    @property
    def directory_path(self) -> Path:
        return Path(self.arguments.directory_path)


class Syamkatze:
    def __init__(self, configuration: Configuration) -> None:
        self.number_of_symlinks: int = 0
        self.number_of_broken_symlinks: int = 0
        self.configuration: Configuration = configuration
        self.search_function: SearchFunction = (
            self.recursive_search if self.configuration.recursive_search else self.non_recursive_search
        )

    @staticmethod
    def recursive_search(directory_path: Path) -> Iterator[Path]:
        for file_path in directory_path.rglob("**/*"):
            if file_path.is_symlink():
                yield file_path

    @staticmethod
    def non_recursive_search(directory_path: Path) -> Iterator[Path]:
        for file_path in directory_path.glob("*"):
            if file_path.is_symlink():
                yield file_path

    @staticmethod
    def delete_symbolic_link(file_path: Path) -> None:
        file_path.unlink()

    @staticmethod
    def introduce_delete_feature() -> None:
        print("To automatically remove broken symbolic links, enable the delete option.")

    @staticmethod
    def introduce_recursive_feature() -> None:
        print("To search recursively, enable the recursive option.")

    @staticmethod
    def introduce_verbose_feature() -> None:
        print("To see detailed information about broken symbolic links, enable verbose option.")

    def increment_symlink_counters(self, is_symlink: bool, is_broken: bool) -> None:
        if is_symlink:
            self.number_of_symlinks += 1
        if is_broken:
            self.number_of_broken_symlinks += 1

    def print_start_message(self) -> None:
        print(f"Searching for symbolic links in {self.configuration.directory_path} ...")

    def print_end_message(self) -> None:
        if self.number_of_symlinks == 0:
            print("No symbolic links found.")
        else:
            self.print_summary()
            if self.number_of_broken_symlinks > 0 and not self.configuration.verbose:
                self.introduce_verbose_feature()
            if self.configuration.delete_symlinks and self.number_of_broken_symlinks > 0:
                self.print_deleted_message()
            else:
                self.introduce_delete_feature()
        if not self.configuration.recursive_search:
            self.introduce_recursive_feature()

    def print_deleted_message(self) -> None:
        print(f"Successfully deleted {self.number_of_broken_symlinks} broken symbolic links.")

    def print_summary(self) -> None:
        print(f"Summary:")
        print(f"    - Total symbolic links found: {self.number_of_symlinks}")
        print(f"    - Broken symbolic links: {self.number_of_broken_symlinks}")

    def run(self) -> None:
        self.print_start_message()
        for file_path in self.search_function(self.configuration.directory_path):
            is_symlink = file_path.is_symlink()
            is_broken = is_symlink and not file_path.exists()
            self.increment_symlink_counters(is_symlink, is_broken)
            if is_symlink:
                if is_broken and self.configuration.delete_symlinks:
                    self.delete_symbolic_link(file_path)
        self.print_end_message()


def main() -> None:
    arguments_parser = ArgumentsParser()
    arguments = arguments_parser.parse()
    configuration = Configuration(arguments)
    syamkatze = Syamkatze(configuration)
    syamkatze.run()


if __name__ == "__main__":
    main()
