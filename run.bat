pytest -v -s -m "sanity" TestCases/ --html=Reports/report.html --browser chrome
Rem pytest -v -s -m "sanity or regression" TestCases/ --html=Reports/report.html --browser chrome
Rem pytest -v -s -m "sanity and regression" TestCases/ --html=Reports/report.html --browser chrome
Rem pytest -v -s -m "regression" TestCases/ --html=Reports/report.html --browser chrome