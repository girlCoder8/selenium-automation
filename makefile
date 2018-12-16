
install: Install
    pip install --upgrade pip
    pip install selenium
	pip install behave
	brew install allure

test: test
	behave -f allure_behave.formatter:AllureFormatter -o ./allure_result ./features/
	allure serve ./allure_result/
