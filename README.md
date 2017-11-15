ISO-3166
===

Country and Subdivision Data

If you have questions or issues with the data I'll do my best to get it updated.
Please create an issue if your find a discrepency.

# Structure
### Raw Data
- `*-raw.json` filescontain lines of json


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
