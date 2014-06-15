#!/usr/bin/env python

import random
import re

class Sweepstake(object):
  """docstring for Sweepspy"""
  
  def __init__(self, teams, people):
    super(Sweepstake, self).__init__()
    self.teams = teams
    self.people = people

  def check_input(self):
    # Need to check if there are more teams than people
    pass

  def _shuffle_teams(self):
    random.shuffle(self.teams)

  def _shuffle_people(self):
    random.shuffle(self.people) 

  def _assign_teams(self):

    self.assigned_teams = {}

    counter = 0
    for team in self.teams:
      person = self.people[counter]

      if person not in self.assigned_teams:
        self.assigned_teams[person] = list()
      
      self.assigned_teams[person].append(team)

      if counter == len(self.people) - 1:
        counter = 0
      else:
        counter += 1

  def _print_assignments(self):

    for person in self.people:
      teams = ''
      for team in self.assigned_teams[person]:
        teams = "%s, %s" % (teams, team.title())

      # Remove comma and whitespace from start of string
      pattern = re.compile(r'^,\s')
      teams = re.sub(pattern, '', teams)

      print "%s: %s" % (person.title(), teams)

  def assign(self):
    self._shuffle_teams()
    self._shuffle_people()
    self._assign_teams()
    self._print_assignments()
