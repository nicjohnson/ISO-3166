ISO-3166
===

Country and Subdivision Data

If you have questions or issues with the data I'll do my best to get it updated.
Please create an issue if your find a discrepancy.

# Introduction
This is a trimmed dataset from the ISO-3166 Country Collection export. I created this to provide data for
dynamic dropdowns in address form fields.

There are a few subdivision categories that have been excluded due to collisions with the country data.
They are not suitable to be used as a selectable option when displaying `states / regions / provinces` in an address form.

#### Excluded Categories
We may exclude more in the future to trim the dataset further
- 241 nation
- 265 outlying areas (as they are also included in the country codes)
- 414 country

# Structure
### Raw Data
- `*-raw.json` files contain lines of json


### Country Data
- `data/countries`
  - `all.json` all countries as a JSON Array

### Subdivision Data

- `data/subdivisions`

  - `all.json` all subdivisions as a JSON Array

  - `grouped.json` all subdivisions as a JSON Object where the keys are Arrays of subdivisions grouped by alpha3 ISO country codes.

  - `by_country`
    - `{country_alpha3}.json}` each file contains a JSON array of subdivisions that match the alpha3 country code in the file name


### Building
All versions of the data will be commited to the repository to track changes.

If you want to generate a fresh copy yourself simply run the build command. This requires `make` and `python 2.7+`. The raw input is stored in the `*-raw.json` files.
```sh
make build
```
