import app

print('example __name__ = %s', __name__)

if __name__=='__main__':
    print('Example is being run directly')

else:
    print('Example is being imported')

# When we run the script with python app.py the __name__ variable will be set to __main__ which indicates we are not using any other file to run this code