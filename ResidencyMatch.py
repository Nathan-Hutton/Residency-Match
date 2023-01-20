'''
ResidencyMatch.py

This algorithm operates by reading an input file of the form

[residents | hospitals] preference 1, preference 2, preference 3, preference 4, ...

Any whitespace occurring in the input files is stripped off.

Usage:

    python ResidencyMatch.py [residents preference file] [hospitals preference file]

Nathan, Greg (not Gagne)

'''

import sys
import csv

class ResidencyMatch:

    # behaves like a constructor
    def __init__(self):
        '''
        Think of
        
            unmatchedHospitals
            residentsMappings
            hospitalsMappings
            matches
            
        as being instance data for your class.
        
        Whenever you want to refer to instance data, you must
        prepend it with 'self.<instance data>'
        '''
        
        # list of unmatched hospitals
        self.unmatchedHospitals = [ ]

        # list of unmatched residents
        self.unmatchedResidents = [ ]
        
        # dictionaries representing preferences mappings
        
        self.residentsMappings = { }
        self.hospitalsMappings = { }
        
        # dictionary of matches where mapping is resident:hospital
        self.matches = { }
        
        # read in the preference files
        
        '''
        This constructs a dictionary mapping a resident to a list of hospitals in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[1],'r'), delimiter = ',')
        for row in prefsReader:
            resident = row[0].strip()

             # all hospitals are initially unmatched
            self.unmatchedResidents.append(resident)

            # maps a resident to a list of preferences
            self.residentsMappings[resident] = [x.strip() for x in row[1:]]
            
            # initially have each resident as unmatched
            self.matches[resident] = None
        
        '''
        This constructs a dictionary mapping a hospital to a list of residents in order of preference
        '''
        
        prefsReader = csv.reader(open (sys.argv[2],'r'), delimiter = ',')
        for row in prefsReader:
            
            hospital = row[0].strip()
            
            # all hospitals are initially unmatched
            self.unmatchedHospitals.append(hospital)
            
            # maps a resident to a list of preferences
            self.hospitalsMappings[hospital] = [x.strip() for x in row[1:]] 
    
            
    def reportMatches(self):
        print(self.matches)
        print('Something')
            
    def runMatch(self):
        hospital_residents = {'CA': None, 'VT': None, 'WA': None, 'NY': None}
        while self.unmatchedResidents:
            for resident in self.unmatchedResidents:
                for pref in self.residentsMappings[resident]:
                    if pref in self.unmatchedHospitals:
                        self.matches[resident] = pref
                        self.unmatchedHospitals.remove(pref)
                        self.unmatchedResidents.remove(resident)
                        hospital_residents[pref] = resident
                        break
                    else:
                        hospital_prefs = self.hospitalsMappings[pref]
                        current_resident = hospital_residents[pref]
                        current_resident_p = hospital_prefs.index(current_resident)
                        possible_resident_p = hospital_prefs.index(resident)
                        if possible_resident_p < current_resident_p:
                            self.matches[resident] = pref
                            self.matches[current_resident] = None
                            self.unmatchedResidents.append(current_resident)
                            self.unmatchedResidents.remove(resident)
                            hospital_residents[pref] = resident
                            break



if __name__ == "__main__":
   
    # some error checking
    if len(sys.argv) != 3:
        print('ERROR: Usage\n python ResidencyMatch.py [residents preferences] [hospitals preferences]')
        quit()

    # create an instance of ResidencyMatch 
    match = ResidencyMatch()

    # now call the runMatch() function
    match.runMatch()
    
    # report the matches
    match.reportMatches()



