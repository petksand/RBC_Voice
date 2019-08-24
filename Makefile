.PHONY: ctrlr voice clean

all:
    docker build -t wholenote_controller ./controller
    docker build -t wholenote_voice ./voice

ctrlr:
	docker run --rm wholenote_controller

voice:
	docker run --rm wholenote_voice
