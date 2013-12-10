from distutils.core import setup
import py2exe

setup(
        console=['eve-bot.py'],
        options={
                "py2exe":{
                        "optimize": 2,
                        "compressed": True,
                        "bundle_files": 2
                }
        }
)
