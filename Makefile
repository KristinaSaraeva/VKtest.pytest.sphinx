all: doc

doc:
	cd docs && make html
	open docs/_build/html/index.html
	
clean:
	make -C docs clean
	rm -rf docs/_build
	rm -rf vk/__pycache__
	rm -rf test/__pycache__