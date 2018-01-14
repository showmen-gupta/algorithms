from utils import Utils
import sys
import csv

class InsertionSort():
    
    def sort(self, dataset):
        utils = Utils()
        for j in range(1,len(dataset)):
            key = dataset[j]
            #insert dataset[j] into sorted sequence dataset[0 ... j-1]
            i = j - 1
            while(i >= 0 and utils.compare(dataset[i], key) > 0):
                dataset[i + 1] = dataset[i]
                i = i - 1
            dataset[i + 1] = key
        return dataset

sortedStudent = [' "Adam Aelia" <a.abuanza@stud.uis.no>', ' "Andreas Kvist" <a.kvist@stud.uis.no>', ' "Antonio Romero Gismera" <a.romerogismera@stud.uis.no>', ' "Azadeh Karimi" <a.karimi@stud.uis.no>', ' "Bilal Amjad" <b.amjad@stud.uis.no>', ' "Denys Chechelnytskyy" <d.chechelnytskyy@stud.uis.no>', ' "Elena Camero Ruiz" <ec.ruiz@stud.uis.no>', ' "Erlend Ådnanes Rekve" <er.rekve@stud.uis.no>', ' "Fredrik Haugsand" <f.haugsand@stud.uis.no>', ' "Hans Ludvig Kleivdal" <hl.kleivdal@stud.uis.no>', ' "Ivan-Louis Miranda Husebø" <im.husebo@stud.uis.no>', ' "Jeyachitra Raghavendran" <j.raghavendran@stud.uis.no>', ' "Jon Arne Bø Hovda" <ja.hovda@stud.uis.no>', ' "Jonatan Pettersen" <j.pettersen@stud.uis.no>', ' "Jorge Andres Thomburne Vidales" <ja.thomburnevidales@stud.uis.no>', ' "Julian Minde" <j.minde@stud.uis.no>', ' "Junaid Alam" <j.alam@stud.uis.no>', ' "Li Deng" <l.deng@stud.uis.no>', ' "Martin Matavka" <m.matavka@stud.uis.no>', ' "Mats Jonassen" <ma.jonassen@stud.uis.no>', ' "Olav Salhus" <o.salhus@stud.uis.no>', ' "Patrick Håland" <p.haaland@stud.uis.no>', ' "Racin Wilhelm Nygaard" <rw.nygaard@stud.uis.no>', ' "Rameesha Asghar" <r.asghar@stud.uis.no>', ' "Ramprasad Beerappa" <r.beerappa@stud.uis.no>', ' "Roberto Augusto Ballestero Bischoff" <ra.ballesterobischoff@stud.uis.no>', ' "Ronny Wathne" <r.wathne@stud.uis.no>', ' "Sandra Moen" <s.moen@stud.uis.no>', ' "Showmen Das Gupta" <sd.gupta@stud.uis.no>', ' "Simon Riis Iden" <sr.iden@stud.uis.no>', ' "Sravya Konda" <s.konda@stud.uis.no>', ' "Sukriti Baniya" <s.baniya@stud.uis.no>', ' "Sunday Eze" <e.sunday@stud.uis.no>', ' "Tomasz Gliniecki" <t.gliniecki@stud.uis.no>', ' "Tor Christian Frausing" <tc.frausing@stud.uis.no>', ' "Vugar Abdul Zada" <v.abdulzada@stud.uis.no>', ' "zubair nawaz" <z.nawaz@stud.uis.no>', 'Jaya Surbiryala <ja.surbiryala@stud.uis.no>']


class TestNumbers():    
    def test_numeric(self):
        iSort = InsertionSort()
        dataset = [2,-3,1,-1,-2,3,0]
        print("IN:\n" + str(dataset))
        rtn = iSort.sort(dataset)
        assert rtn == [-3,-2,-1,0,1,2,3]
        print("OUT:\n" + str(rtn))
        

class TestStudents():      
    def test_student(self): 
        iSort = InsertionSort() 
        #Data is stored in one line with each value seperated by a semicolon
        path = '/home/antorweep/Documents/git/AlgorithmTheory_DAT600_Spring2017_University_of_Stavanger/'
        with open(path + 'students_worse.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            lines = list(reader)
        dataset =  lines[0]
        print("IN:\n" + str(dataset))
        rtn = iSort.sort(dataset)
        assert rtn == sortedStudent
        print("OUT:\n" + str(rtn))
        