
# minimal examples

A collection of small code examples, which can be used for learning syntax and idiosyncrasies.
You can use the examples to memorize features of programming languages.
A *spaced repetition software* (SRS) such as [Anki](https://apps.ankiweb.net/) might help with that task.

Currently there are examples for
* python3
* latex
* rust
* web development (web_dev)

Screenshot of a flash card in Anki:

![Screenshot](https://raw.githubusercontent.com/thomasrebele/minimal_examples/master/images/screenshot0.png)
![Screenshot](https://raw.githubusercontent.com/thomasrebele/minimal_examples/master/images/screenshot1.png)


## Level assessment

Some examples are more difficult to understand.
Therefore this project also aims to provide a method to sort them according to their level (difficulty).
To assign a level to examples interactively, you can use the following command:

    python3 level_assessment.py  <example-files>

The command will start a browser. You are presented with two cards. You select which of them is easier. 
All decisions are stored in `output/level_data.json`.
The script `level_estimate.py` calculates a level based on these decisions.


## Generating the cards

The script `generate_cards.py` converts the examples to flash cards.
It uses the levels (see previous section) to sort the cards by difficulty.
To generate the cards, use the command

    python3 generate_cards.py  <example-files>  >  <output-file>

Problems are reported to standard error. 
The output is a file in the TSV (tab separated value) format.
Its columns are

* example: a unique identifier
* description
* pre: code that precedes the code that the user has to remember
* step: this is the code that the user needs to know
* post: code that shows how to apply the result
* explanation: give more detail for for non-obvious/counter-intuitive answers


## Importing into Anki

1. Choose File -> Import 
2. Select the right type and deck (this project might provide a template at a later stage)
3. "Fields separated by: Tab"
4. "Update existing notes when first field matches"
5. Activate "Allow HTML in fields"
6. Map the columns
7. Click on "Import"

Note that the order of already imported cards does not change.
This could be achieved by an Anki add-on. Any help is appreciated.

## Contributions

You can contribute in several ways:

* give feedback on usability
* provide examples for existing programming languages
* add new programming languages
* write addons for better integration with SRS (especially Anki)
* ...

Any contribution shall be licensed by the same license as the project, see the [license](#license) section below.

## Acknowledgements

Logos:

* Rust: https://www.rust-lang.org/en-US/legal.html
* Python: https://www.python.org/community/logos/
* Git: https://git-scm.com/downloads/logos

## License

This project is licensed under the AGPL, version 3 ([LICENSE](LICENSE) or https://www.gnu.org/licenses/agpl-3.0.en.html).

## Disclaimer

The examples are provided WITHOUT ANY WARRANTY; 
without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
The use of the logos of the programming languages (Python, Rust, ...)
is for visual purposes only. It does not imply any endorsement by the respective projects.


