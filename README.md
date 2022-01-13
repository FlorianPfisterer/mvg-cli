# MVG-cli
A CLI tool for easy access to live MVG (Munich public transport) data from the command line.
![A screenshot of the Terminal where the `mvg` command is run](./example.png)

## Installation
`pip install mvg-cli`

## Why?
When I want to catch the train to go to university or to the city, I need to check the upcoming departures with live delay data of the Munich metro at my local metro station. Using the MVG app or website is a bit cumbersome for this use case.

Obviously, the only sensible solution is to create a CLI tool that makes it super convenient to get live data about upcoming departures right from the Terminal.

## Usage
The basic idea is that you can define your favorite routes (start and destination stations) and then get the current departures by just typing `mvg` (just like in the screenshot at the top).
In addition to managing your favorites, the CLI also allows manual querying.

### Manual Querying
You can do manual queries for upcoming departures from a given metro station in the MVG system. The basic syntax in this case is:
```text
mvg -f <start station> [-t <destination station>] [-o <offset>] [-l <limit>]
```
The `-f` / `--from` parameter ('from') is required. Specify the starting train station which you're interested in, e.g., 'Marienplatz'. Optionally, you can also supply:
* `-t` / `--to`: filter the departures by their final destination station (simple string matching)
* `-o` / `--offset`: offset the departures by a number of minutes (e.g., in how many minutes you will be at the station)
* `-l` / `--limit`: limit the number of results (5 by default)

For example, to query upto 7 departures from 'Marienplatz' having 'Garching' in their name and leaving in at least 5min, you would use
```text
mvg -f Marienplatz -t Garching -o 5 -l 7
```

### Favorites
If you just run `mvg`, your favorite queries will be executed and displayed. A favorite query has just the same properties as a manual query (described above). To manage your favorites, use these commands:

**Listing your favorites**
```text
mvg favorites list
```

**Adding a favorite**
```text
mvg favorites add -f <start station> [-t <destination station>] [-o <offset>] [-l <limit>]
```
Using the same parameters as the manual query method described above.

**Removing a favorite**
```text
mvg favorites remove -i <index>
```
When listing your favorites, each entry will have a 0-based index. Specify this index of the favorite you want to remove.

### Defaults
Currently, only one configuration setting is available: in order to get colored departure results (green if you will catch it easily, orange if it's going to be close and red if it's probably not going to be enough), you need to define how many minutes it will approximately take you to the station. For example, if it takes you about 5min, run:

```text
mvg defaults time-to-station 5
```

Subsequent manual and favorite queries will be colorized accordingly.

## Important Legal Note
The CLI uses the [mvg_api](https://github.com/leftshift/python_mvg_api) library, which in turn queries the MVG JSON API. This only allows private, non-commercial and moderate use. Do not use it for data mining. I'm not a lawyer and this is not legal advice. Please check the [official terms of service](https://www.mvg.de/impressum.html).

## Upcoming Features

- [ ] use the MVG JSON API directly to allow for better pagination and station selection
- [ ] add more sophisticated routing features (i.e., not just start and destination station but arbitrary stations in the metro system)
- [ ] document the code better

## Acknowledgements
Among other dependencies, this project is mainly based on the [mvg_api](https://github.com/leftshift/python_mvg_api) library by [leftshift](https://github.com/leftshift) to query the MVG API.

## Contributing
The CLI is structued in an extensible manner by design, as I think a lot of very useful features could be added in the future (see 'Upcoming Features' above). I'm very happy to accept contributions!

The code is currently not documented very well since it was hacked together in a few hours, so if you need some pointers or want to discuss your idea, feel free to reach out! You'll find my contact info on [my website](https://pfisterer.dev).
