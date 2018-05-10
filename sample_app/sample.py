import sample_library.sample as sample

def use_library():
    foo = sample.read()
    return foo

if __name__ == '__main__':
    use_library()
