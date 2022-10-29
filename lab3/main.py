from LexicalRunner import LexicalRunner

if __name__ == '__main__':
    scanner_result = LexicalRunner()
    scanner_result.run("files/p1.txt")
    scanner_result.run("files/p3.txt")
    scanner_result.run("files/p1Err.txt")