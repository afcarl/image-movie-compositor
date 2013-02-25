frames: imgs/*
	python writer.py

movie: frames
	mplayer "mf://frames/*.png" -mf fps=10 -vo yuv4mpeg:file="/tmp/tmp.y4m" -ao null -nosound -noframedrop -benchmark -nolirc
	x264 --profile baseline /tmp/tmp.y4m -o movie.mp4
	ffmpeg2theora --videobitrate 1000 --optimize movie.mp4 -o movie.ogv

clean:
	rm -f frames/*

test:
	rm -f test/imgs/*
	rm -f test/frames/*
	IDIR=test/imgs python test/genimages.py
	IDIR=test/imgs ODIR=test/frames python writer.py
	mplayer "mf://test/frames/*.png" -mf fps=10 -vo yuv4mpeg:file="/tmp/ttmp.y4m" -ao null -nosound -noframedrop -benchmark -nolirc
	x264 --profile baseline /tmp/ttmp.y4m -o test/movie.mp4
	ffmpeg2theora --videobitrate 1000 --optimize test/movie.mp4 -o test/movie.ogv

.PHONY: test clean
