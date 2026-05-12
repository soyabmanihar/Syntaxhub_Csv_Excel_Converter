import pandas as pd
import argparse
import logging
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def clean_column_names(columns):
    """
    Normalize column names:
    - lowercase
    - replace spaces with underscores
    - strip whitespace
    """
    return [col.strip().lower().replace(" ", "_") for col in columns]


def parse_dates(df):
    """
    Attempt to parse date columns automatically.
    """
    for column in df.columns:
        try:
            df[column] = pd.to_datetime(df[column])
        except Exception:
            pass
    return df


def handle_missing_values(df):
    """
    Fill missing values:
    - numeric columns -> 0
    - object/string columns -> 'Unknown'
    """
    for column in df.columns:
        if df[column].dtype == "object":
            df[column] = df[column].fillna("Unknown")
        else:
            df[column] = df[column].fillna(0)

    return df


def rename_columns(df, rename_pairs):
    """
    Rename columns from CLI input.
    Example:
    name=full_name,age=user_age
    """
    rename_dict = {}

    if rename_pairs:
        pairs = rename_pairs.split(",")

        for pair in pairs:
            if "=" in pair:
                old, new = pair.split("=")
                rename_dict[old.strip()] = new.strip()

    return df.rename(columns=rename_dict)


def convert_csv_to_excel(input_file, output_file, rename_pairs=None):
    """
    Main conversion function.
    """

    # Validate file existence
    if not os.path.exists(input_file):
        logging.error(f"Input file not found: {input_file}")
        return

    try:
        logging.info("Reading CSV file...")
        df = pd.read_csv(input_file)

        logging.info("Cleaning column names...")
        df.columns = clean_column_names(df.columns)

        logging.info("Handling missing values...")
        df = handle_missing_values(df)

        logging.info("Parsing date columns...")
        df = parse_dates(df)

        logging.info("Renaming columns...")
        df = rename_columns(df, rename_pairs)

        logging.info("Exporting to Excel...")
        df.to_excel(output_file, index=False, engine="openpyxl")

        logging.info(f"Conversion successful: {output_file}")

    except pd.errors.EmptyDataError:
        logging.error("The CSV file is empty.")

    except pd.errors.ParserError:
        logging.error("Error parsing CSV file. Check file format.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="CSV to Excel Converter"
    )

    parser.add_argument(
        "-i",
        "--input",
        default="sample.csv",
        help="Path to input CSV file (default: sample.csv)"
    )

    parser.add_argument(
        "-o",
        "--output",
        default="output.xlsx",
        help="Path to output Excel file (default: output.xlsx)"
    )

    parser.add_argument(
        "-r",
        "--rename",
        default=None,
        help="Rename columns. Example: name=full_name,age=user_age"
    )

    args = parser.parse_args()

    convert_csv_to_excel(
        args.input,
        args.output,
        args.rename
    )


if __name__ == "__main__":
    main()
