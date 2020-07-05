BUILD_DIR=./_build
VENV_DIR=${BUILD_DIR}/venv
SHELL := /bin/bash

ALL_DIRS := $(wildcard *)
EXCLUSIONS := Makefile _build
PACKAGES := $(filter-out $(EXCLUSIONS), $(ALL_DIRS))

test: $(patsubst %,test-%,$(PACKAGES))

dev-%:
	echo $@
	#echo ${PACKAGES}

build_dir:
	mkdir -p ${BUILD_DIR}

venv_dir: build_dir
	python3 -m venv ${VENV_DIR}

copy-src-%: venv_dir
	cp -r $(subst copy-src-,,$@) ${BUILD_DIR}

build-%: venv_dir copy-src-%
	source ${VENV_DIR}/bin/activate &&\
	pip3 install -r $(subst build-,,$@)/requirements.txt

test-%: build-%
	echo $(subst test-,,$@) #target_name
	source ${VENV_DIR}/bin/activate &&\
	cd  ${BUILD_DIR}/$(subst test-,,$@) &&\
	tox

clear:
	rm -rf ${VENV_DIR}/*
	rm -rf ${BUILD_DIR}/*
