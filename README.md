# roll20_macros
Generate diverse macros for your roll20 D&amp;D games

Usage:

```
python generate_macros.py --help
usage: generate_macros.py [-h] [-p] [-c CHARACTERS [CHARACTERS ...]]

optional arguments:
  -h, --help            show this help message and exit
  -p, --player          Generate only for players
  -c CHARACTERS [CHARACTERS ...], --characters CHARACTERS [CHARACTERS ...]
                        Generate macros for the specified characters. If not specified it will only generate selected token macros. Multiple characters can be specified
```

By default it will print the macros. It is recommended to save the output into a file and copy them from it:

```
python generate_macros.py --characters "Lorem Ipsum" "Aurora Borealis" > macros.txt
```

By default macros will be generated for DMs, meaning that the "singular" macros use the *selected token* as a target.
If the character names are specified, the "group" macros will target all the characters.

## Macros for players

Generating the macros for players will generate the "singular" macros using the specified characters as a target.

## Specify characters

You can use `--characters [Character name list]` (separated by `,`, the `"` are required in order to get the whole character name)

> TODO: Also accept `--characters_file <Path to a file containing all the character names>`.

If no characters are specified, it will generate macros for the *selected token* as a target.

## Available Macros

> Do you have a suggestion? Open an [issue](https://github.com/ytturi/roll20_macros/issues/new/choose)!

### Singular Macros

#### Roll

- Initiative: Uses the default character method to roll initiative: `%{selected|npc_init}`
- Ability check: [Based on a macro in the roll20 forum](https://app.roll20.net/forum/post/5591522/5e-ogl-universal-ability-check-macro-updated-for-v2-dot-0) By Kyle G. (Original by Craig)
- Saving Throw: [Based on a macro in the roll20 forum](https://app.roll20.net/forum/post/5591512/5e-ogl-universal-saving-throw-macro-updated-for-v2-dot-0) By Kyle G. (Original by Craig)
- Skill check: [Based on a macro in the roll20 forum](https://app.roll20.net/forum/post/5591526/5e-ogl-universal-skill-check-macro-updated-for-v2-dot-0) By Craig

### Group Macros

- Passive perception
- Total weight
