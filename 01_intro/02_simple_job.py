from mrjob.job import MRJob

class MrSimpleJob(MrJob):
    def mapper(self, _,value):
        yield 'line', 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MrSimpleJob.run()
