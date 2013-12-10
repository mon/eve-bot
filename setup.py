from distutils.core import setup
import py2exe

setup(
        console=['eve-bot.py'],
        options={
                "py2exe":{
                        "optimize": 2,
                        "includes": ["Mumble_pb2"],
                        "bundle_files": 2
                }
        }
)
