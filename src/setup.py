#!/usr/bin/env python

if __name__ == "__main__":

	from distutils.core import setup

	setup(name="footpedal",
		description="USB foot pedal integration for Gnome desktops",
		long_description="""footpedal acts as a "pseduo-driver" for the USB foot pedal for
transcriptionists by VEC. It lets you assign arbitrary keystrokes to the left,
middle, and right pedal. It might also work with a home-built USB foot pedal.""",
		author="Karl Ostmo",
		author_email="kostmo@gmail.com",
		url="http://footpedal.googlecode.com/",
		version="0.5",
		scripts=["footpedal"],
		data_files=[("share/footpedal", ["foot_up.png", "foot_down.png", "footpedal.png"])]
	)


