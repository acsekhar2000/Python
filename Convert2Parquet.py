from pyspark.sql import SparkSession
import sys
import os

def csv_to_parquet(input_csv_path, output_parquet_path):
    """
    Converts a CSV file to Parquet format using PySpark.
    Args:
        input_csv_path (str): Path to the input CSV file.
        output_parquet_path (str): Path to save the output Parquet file.
    """
    # Validate input file
    print(input_csv_path)
    if not os.path.isfile(input_csv_path):
        print(f"Error: CSV file '{input_csv_path}' does not exist.")
        sys.exit(1)

    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("CSV to Parquet Converter") \
        .getOrCreate()

    try:
        # Read CSV with header and schema inference
        df = spark.read.csv(
            input_csv_path,
            header=True,       # First row as header
            inferSchema=True   # Automatically detect column types
        )

        # Show a preview of the data
        print("Preview of CSV data:")
        df.show(5)

        # Write DataFrame to Parquet format
        df.write.mode("overwrite").parquet(output_parquet_path)

        print(f"✅ Successfully converted '{input_csv_path}' to Parquet at '{output_parquet_path}'")

    except Exception as e:
        print(f"Error during conversion: {e}")
        sys.exit(1)
    finally:
        spark.stop()


if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 3:
        print("Usage: python csv_to_parquet.py <input_csv_path> <output_parquet_path>")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_parquet = sys.argv[2]
    print(input_csv)
    print(sys.argv[2])


    csv_to_parquet(input_csv, output_parquet)
