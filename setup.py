from distutils.core import setup
import py2exe

setup(
        console=['eve-bot.py'],
        options={
                "py2exe":{
                        #"unbuffered": True,
                        #"optimize": 2,
                        "includes": ["Mumble_pb2"]
                        #"excludes": ["email"]
                }
        }
)
