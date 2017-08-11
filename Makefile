

test:
	pycodestyle --max-line-length=160 --config=/dev/null --ignore=E305,E402,E722,E741 library/ module_utils/
	python -m compileall library/ module_utils/

