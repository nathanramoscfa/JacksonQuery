from jacksonquery import source_extractor
from jacksonquery import classification_schema
from jacksonquery import prospectus_extractor
from jacksonquery import stats_extractor
from portfolio_optimization import factor_data
from portfolio_optimization import factor_model


def main():
    # Run the source extractor and store its results
    source_extractor.get_page_source()

    # Run the classification schema and store its results
    classification_schema.classification_schema()

    # Run the prospectus scraper and store its results
    fees, returns_A, returns_I, tenures, turnovers = prospectus_extractor.run_prospectus_extractor()


if __name__ == "__main__":
    main()
