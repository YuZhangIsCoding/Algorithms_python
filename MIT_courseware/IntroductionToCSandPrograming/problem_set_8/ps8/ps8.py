# 6.00 Problem Set 8
#
# Name:
# Collaborators:
# Time:



import numpy
import random
import pylab
import pdb
from ps7 import *

#
# PROBLEM 1
#
class ResistantVirus(SimpleVirus):

    """
    Representation of a virus which can have drug resistance.
    """      

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):

        """

        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'grimpex',False}, means that this virus
        particle is resistant to neither guttagonol nor grimpex.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.        

        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb


    def isResistantTo(self, drug):

        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in Patient to determine how many virus
        particles have resistance to a drug.    

        drug: The drug (a string)
        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.resistances.get(drug, False)


    def reproduce(self, popDensity, activeDrugs):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient class.

        If the virus particle is not resistant to any drug in activeDrugs,
        then it does not reproduce. Otherwise, the virus particle reproduces
        with probability:       
        
        self.maxBirthProb * (1 - popDensity).                       
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb and clearProb values as its parent). 

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.        

        For example, if a virus particle is resistant to guttagonol but not
        grimpex, and `self.mutProb` is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90% 
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        grimpex and a 90% chance that the offspring will not be resistant to
        grimpex.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population        

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings). 
        
        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.         
        """
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                raise NoChildException()
        if random.random() <= self.maxBirthProb*(1-popDensity):
            res = {}
            for resname in self.resistances:
                if random.random() <= self.mutProb:
                    res[resname] = not self.resistances[resname]
                else:
                    res[resname] = self.resistances[resname]
            return ResistantVirus(self.maxBirthProb, self.clearProb, \
                                  res, self.mutProb)
        else:
            raise NoChildException()

class Patient(SimplePatient):

    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).               

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        
        maxPop: the  maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []
    

    def addPrescription(self, newDrug):

        """
        Administer a drug to this patient. After a prescription is added, the 
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: list of drugs being administered to a patient is updated
        """
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):

        """
        Returns the drugs that are being administered to this patient.
        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.drugs
        
    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in 
        drugResist.        

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'grimpex'])

        returns: the population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        count = 0
        for virus in self.viruses:
            for drug in drugResist:
                if not virus.isResistantTo(drug):
                    count += 1
                    break
        return len(self.viruses)-count

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:
        
        - Determine whether each virus particle survives and update the list of 
          virus particles accordingly          
        - The current population density is calculated. This population density
          value is used until the next call to update().
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient. 
          The listof drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces. 

        returns: the total virus population at the end of the update (an
        integer)
        """
        temp = []
        for virus in self.viruses:
            if not virus.doesClear():
                temp.append(virus)
        curPop = len(temp)*1.0/self.maxPop
        offspring = []
        for virus in temp:
            try:
                offspring.append(virus.reproduce(curPop, self.drugs))
            except NoChildException:
                pass
        self.viruses = temp+offspring
        return self.getTotalPop()
            

#
# PROBLEM 2
#

def simulationWithDrug():

    """

    Runs simulations and plots graphs for problem 4.
    Instantiates a patient, runs a simulation for 150 timesteps, adds
    guttagonol, and runs the simulation for an additional 150 timesteps.
    total virus population vs. time and guttagonol-resistant virus population
    vs. time are plotted
    """
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False}
    mutProb = 0.005
    num_trials = 100
    pop_avg = numpy.zeros(300)
    pop_res_avg = numpy.zeros(150)
    for trial in range(num_trials):
        patient = Patient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*100,\
                          1000)
        time = range(150)
        pop = [patient.getTotalPop()]
        for i in time[1:]:
            pop.append(patient.update())
        patient.addPrescription('guttagonol')
        pop_res = []
        for i in time:
            pop.append(patient.update())
            pop_res.append(patient.getResistPop(patient.getPrescriptions()))
        pop_avg += numpy.array(pop)
        pop_res_avg += numpy.array(pop_res)
    pop_avg /= 1.0*num_trials
    pop_res_avg /= 1.0*num_trials
    pylab.plot(range(300), pop_avg, 'o', mfc = 'w', mec = 'b', label = 'total virus')
    pylab.plot(range(150, 300), pop_res_avg, 'o', mfc = 'w', mec = 'r', label = 'g-resistant virus')
    pylab.title('virus population vs. time')
    pylab.legend(loc = 'best')
    pylab.xlabel('time')
    pylab.ylabel('virus population')
    pylab.xlim([-10, 310])
    pylab.ylim([-10, 600])
    pylab.grid()
    pylab.savefig('problem_2.pdf')

#simulationWithDrug()

#
# PROBLEM 3
#

def simulationDelayedTreatment():

    """
    Runs simulations and make histograms for problem 5.
    Runs multiple simulations to show the relationship between delayed treatment
    and patient outcome.
    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).    
    """
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol':False}
    mutProb = 0.005
    num_trials = 100
    fig = pylab.figure(figsize = (14, 7))
    ax0 = pylab.subplot2grid((7, 4), (0, 0), rowspan = 4, colspan = 4)
    color = ['r','b','g','purple']
    axes = []
    for seq, delay in enumerate([300, 150, 75, 0]):
        pop_avg = numpy.zeros(delay+150)
        pop_res_avg = numpy.zeros(150)
        pop_fin = []
        for trial in range(num_trials):
            patient = Patient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*100,\
                              1000)
            time1 = range(delay)
            pop = []
            for i in time1:
                pop.append(patient.getTotalPop())
                patient.update()
            time2 = range(delay, delay+150)
            patient.addPrescription('guttagonol')
            pop_res = []
            for i in time2:
                pop.append(patient.getTotalPop())
                pop_res.append(patient.getResistPop(patient.getPrescriptions()))
                patient.update()
            pop_avg += numpy.array(pop)
            pop_res_avg += numpy.array(pop_res)
            pop_fin.append(pop[-1])
        pop_avg /= 1.0*num_trials
        pop_res_avg /= 1.0*num_trials
        ax0.plot(time1+time2, pop_avg, 'o', mfc = 'w', mec = color[seq], label = str(delay), alpha = 0.5)
        ax0.plot(time2, pop_res_avg, 's', mfc = 'w', mec = color[seq], label = str(delay))
        ax = pylab.subplot2grid((7, 4), (4, seq), rowspan = 3)
        axes.append(ax)
        ax.hist(pop_fin)
        ax.set_xlabel('Virus Pop')
        xlim = int(min(pop_fin)*0.9/10)*10
        xmax = int(max(pop_fin)*1.1/10)*10
        ax.set_xlim(xlim, xmax)
        ax.set_xticks(numpy.arange(xlim, xmax, 100))
    axes[0].set_ylabel('Patients')
    ax0.set_title('virus population vs. time')
    ax0.legend(loc = 'center', bbox_to_anchor = (0.5, 1), ncol = 4)
    ax0.set_xlabel('time')
    ax0.set_ylabel('virus population')
    ax0.set_xlim(-10)
    ax0.set_ylim(-10)
    pylab.tight_layout(w_pad = 0, h_pad = 0.5)
    pylab.savefig('problem_3.pdf')
    
#simulationDelayedTreatment()

#
# PROBLEM 4
#

def simulationTwoDrugsDelayedTreatment():

    """
    Runs simulations and make histograms for problem 6.
    Runs multiple simulations to show the relationship between administration
    of multiple drugs and patient outcome.
   
    Histograms of final total virus populations are displayed for lag times of
    150, 75, 0 timesteps between adding drugs (followed by an additional 150
    timesteps of simulation).
    """
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    num_trials = 30
    fig = pylab.figure(figsize = (14, 7))
    ax0 = pylab.subplot2grid((7, 4), (0, 0), rowspan = 4, colspan = 4)
    color = ['r','b','g','purple']
    axes = []
    for seq, delay in enumerate([300, 150, 75, 0]):
        pop_avg = numpy.zeros(delay+300)
        pop_res_avg = numpy.zeros(delay+150)
        pop_fin = []
        for trial in range(num_trials):
            patient = Patient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*100,\
                              1000)
            time1 = range(150)
            pop = []
            for i in time1:
                pop.append(patient.getTotalPop())
                patient.update()
            time2 = range(150, delay+150)
            patient.addPrescription('guttagonol')
            pop_res = []
            for i in time2:
                pop.append(patient.getTotalPop())
                pop_res.append(patient.getResistPop(patient.getPrescriptions()))
                patient.update()
            time3 = range(delay+150, delay+300)
            patient.addPrescription('grimpex')
            for i in time3:
                pop.append(patient.getTotalPop())
                pop_res.append(patient.getResistPop(patient.getPrescriptions()))
                patient.update()
            pop_avg += numpy.array(pop)
            pop_res_avg += numpy.array(pop_res)
            pop_fin.append(pop[-1])
        pop_avg /= 1.0*num_trials
        pop_res_avg /= 1.0*num_trials
        ax0.plot(time1+time2+time3, pop_avg, 'o', mfc = 'w', mec = color[seq], label = str(delay), alpha = 0.5)
        ax0.plot(time2+time3, pop_res_avg, 's', mfc = 'w', mec = color[seq], label = str(delay))
        ax = pylab.subplot2grid((7, 4), (4, seq), rowspan = 3)
        axes.append(ax)
        ax.hist(pop_fin)
        ax.set_xlabel('Virus Pop')
        xlim = int(min(pop_fin)*0.9/10)*10
        xmax = int(max(pop_fin)*1.1/10)*10
        ax.set_xlim(xlim, xmax)
        ax.set_xticks(numpy.arange(xlim, xmax, 100))
    axes[0].set_ylabel('Patients')
    ax0.set_title('virus population vs. time')
    ax0.legend(loc = 'center', bbox_to_anchor = (0.5, 1), ncol = 4)
    ax0.set_xlabel('time')
    ax0.set_ylabel('virus population')
    ax0.set_xlim(-10)
    ax0.set_ylim(-10)
    pylab.tight_layout(w_pad = 0, h_pad = 0.5)
    pylab.savefig('problem_4.pdf')

#simulationTwoDrugsDelayedTreatment()
#
# PROBLEM 5
#    

def simulationTwoDrugsVirusPopulations():

    """

    Run simulations and plot graphs examining the relationship between
    administration of multiple drugs and patient outcome.
    Plots of total and drug-resistant viruses vs. time are made for a
    simulation with a 300 time step delay between administering the 2 drugs and
    a simulations for which drugs are administered simultaneously.        

    """
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    num_trials = 30
    color1 = ['r','b']
    color2 = ['pink', 'cornflowerblue']
    color3 = ['darkred', 'darkblue']
    axes = []
    for seq, delay in enumerate([300, 0]):
        pop_avg = numpy.zeros(delay+300)
        pop_res_avg = numpy.zeros(delay+150)
        pop_res_1_avg = numpy.zeros(delay+150)
        pop_res_2_avg = numpy.zeros(150)
        for trial in range(num_trials):
            patient = Patient([ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)]*100,\
                              1000)
            time1 = range(150)
            pop = []
            for i in time1:
                pop.append(patient.getTotalPop())
                patient.update()
            time2 = range(150, delay+150)
            patient.addPrescription('guttagonol')
            pop_res = []
            pop_res_1= []
            pop_res_2 = []
            for i in time2:
                pop.append(patient.getTotalPop())
                pop_res.append(patient.getResistPop(patient.getPrescriptions()))
                pop_res_1.append(patient.getResistPop(['guttagonol']))
                patient.update()
            time3 = range(delay+150, delay+300)
            patient.addPrescription('grimpex')
            for i in time3:
                pop.append(patient.getTotalPop())
                pop_res.append(patient.getResistPop(patient.getPrescriptions()))
                pop_res_1.append(patient.getResistPop(['guttagonol']))
                pop_res_2.append(patient.getResistPop(['grimpex']))
                patient.update()
            pop_avg += numpy.array(pop)
            pop_res_avg += numpy.array(pop_res)
            pop_res_1_avg += numpy.array(pop_res_1)
            pop_res_2_avg += numpy.array(pop_res_2)
        pop_avg /= 1.0*num_trials
        pop_res_avg /= 1.0*num_trials
        pop_res_1_avg /= 1.0*num_trials
        pop_res_2_avg /= 1.0*num_trials
        pylab.plot(time1+time2+time3, pop_avg, 'o', mfc = 'w', mec = color1[seq], label = 'tt '+str(delay), alpha = 0.3)
        pylab.plot(time2+time3, pop_res_avg, 's', mfc = 'w', mec = color1[seq], label = 'tr '+str(delay))
        pylab.plot(time2+time3, pop_res_1_avg, '^', mfc = 'w', mec = color2[seq], label = 'r1 '+str(delay))
        pylab.plot(time3, pop_res_2_avg, 'v', mfc = 'w', mec = color3[seq], label = 'r2 '+str(delay))
    pylab.legend(loc = 'best', ncol = 2)
    pylab.savefig('problem_5.pdf')

#simulationTwoDrugsVirusPopulations()
