batbot
======

Makes a joke on reddit when appropriate. If someone on the front page says "I swear to God" batbot will reply "SWEAR TO ME".

Examples: http://www.reddit.com/user/swear_to_who

I realize it should be "whom".

To run fill in a valid username and password in `secrets.py`. 

```
python batbot.py --monitor
```

Custom stimuli and response can be specified with `--stimulus` and `--response`.

For example:
```
python batbot.py --monitor --stimulus "source: I am a" --response "But it's not who you are underneath, it's what you do that defines you."
```
