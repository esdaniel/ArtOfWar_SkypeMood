## Skype Mood 'Art of War' quotes

Just a bit of fun I hacked together to post random Art of War quotes to my Skype mood status.

### Prerequisites

* Python v3+
* Skype
* Dbus

### Installing

It's just a couple of python scripts and a text file, so place in any directory of your choosing:

```
$ git clone https://github.com/esdaniel/ArtOfWar_SkypeMood
$ cd ArtOfWar_SkypeMood
$ chmod a+x ./artofwar_skypemood.py
```

Log in to Skype, go to *Options>Public API* and ensure *DBUS* is enabled. Then run the script from the command line:

```
$ ./artofwar_skypemood.py
```

Skype will display a dialog box requesting permission to allow API access from *skype_mood.py*, click *yes* and you're good to go. Skype will remember the request for future use, you can check *>Options>Public API* to confirm this is so. 

### Running the script

```$ ./artofwar_skypemood.py```

### Cron job

If you want to call the script from a cron job ensure you have enabled execution bit of *artofwar_skypemood.py* with ```$ chmod a+x ./artofwar_skypemood.py``` and your cron job should look something like this:
```05 */1 * * * export DISPLAY=:0 && <script installation directory>/artofwar_skypemood.py```

### License

[Creative Commons Attribution 3.0 license](http://creativecommons.org/licenses/by/3.0/us/deed.en_US)

### Acknowledgements

* Thanks to Af for inadvertently giving me the idea ;-)
* Thanks to [Joshua Arrington](https://blog.arrington.me) for sharing the skype_mood module
* Thanks to [ArtofWarQuotes.com](http://www.artofwarquotes.com/) for... the quotes
