from utils import *

def main():
    job_id = int(os.environ['JOB_ID'])
    DATA_DIR = '/datasets/cifar10-data'

    f = open(DATA_DIR+"/output.txt")
    f.write("Ellison {} was here!".format(job_id))
    f.close()

if __name__ == '__main__':
    main()

