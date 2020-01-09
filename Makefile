build:
	@echo "building binary"
	go build -o bin/server server.go

clean:
	rm bin/*
