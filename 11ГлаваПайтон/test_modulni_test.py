import modulni_test
try:
    assert modulni_test.get_city("kz", "ast") == "Kaz Ast"
except AssertionError:
    print("test 1 N")
    assert modulni_test.get_cit("kaz", "ast", "1000") == "Kaz Ast 1000"


