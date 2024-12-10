## Welcome to the OSU!CBMSD
Its free open-source project to download maps directly (using catboy.best mirror)
Or random thing that allowes you download beatmaps fast.

## How to run?
Just download it from [releases](https://github.com/Corrupted-Code/osu-cbmsd/releases) or you can run it from source code.

And you need [tampermonkey](https://www.tampermonkey.net/), [violentmonkey](https://chromewebstore.google.com/detail/violentmonkey/jinjaccalgkegednnccohejagnlnfdag?hl=ru&pli=1) or something like this with our [script](https://github.com/Corrupted-Code/osu-cbmsd/releases/download/v0.0.1/cbmsd.user.js) installed.

## Running
1. Clone repository (``git clone https://github.com/Corrupted-Code/osu-cbmsd``)
2. Install python libs (``pip install -r requirements.txt``)
3. Run the code. (``python cbmsd.py``)

## Building
You can build it using nuitka.
just run ``nuitka --standalone --onefile --include-package=cbmsd cbmsd.py`` (with installed nuitka.)
