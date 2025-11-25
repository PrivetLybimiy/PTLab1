from DataReader import DataReader


class YamlDataReader(DataReader):

    def read(self, path):
        students = {}
        name = ''

        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line.startswith('-'):
                    name = line[1:].strip().rstrip(':')
                    students[name] = []

                elif name and ':' in line:
                    subject, mark = line.split(':', maxsplit=1)
                    students[name].append((subject.strip(), int(mark.strip())))

        return students
