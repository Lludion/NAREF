#!/usr/bin/env python
"""
Defines the default data (mackey, sine ...) and initial Forecaster parameters
"""
from reservoirpy.datasets import mackey_glass
from sklearn.preprocessing import MinMaxScaler
import numpy as np


class Dataset:
	def __init__(self):
		"""
		This dataset class contains several variables representing a TSP dataset and reservoir parameters
		"""
		# Choose input data: mackey glass ('mackey') or sine curve ('sine')
		self.input_type = "mackey"

		# MACKEY_GLASS
		# create a simple mackey_glass time series, rescaled between 0.2 and 1 for encoding
		self.mackey = mackey_glass(2000)
		scaler = MinMaxScaler(feature_range=(0.2, 1))
		scaler.fit(self.mackey)
		# we noticed that the typo on the following line meant that the rescaling was not applied in our calculations.
		# to make our results reproducible, we decided to provide an unscaled version of this feature in the package.
		self.umackey = mackey_glass(2000) # unscaled mackey
		self.mackey = scaler.transform(self.mackey)

		# SINE
		self.sine = np.sin(np.linspace(0, 6 * np.pi, 600)).reshape(-1, 1)
		scaler = MinMaxScaler(feature_range=(0.2, 1))
		scaler.fit(self.sine)
		self.sine = scaler.transform(self.sine)

		# split input_type into train and test
		if self.input_type == 'mackey':
			self.base_data = self.mackey
		elif self.input_type == 'umackey':
			self.base_data = self.umackey
		else:
			self.base_data = self.sine

		self.inp_train = self.base_data[:250]
		self.inp_test = self.base_data[250:280]

		# These are the default fixed hyperparameters
		# Use Comparator.hyper if you want to do an exhaustive hyperparameter search

		self.train_len = len(self.inp_train)
		self.test_len = len(self.inp_test)
		self.sample_len = 8

		# Not implemented yet : different values for N_samples, sample_len and reset_rate for train and test phases.

		# Classical Reservoir Parameters
		self.nb_neurons = 9

		# Quantum Reservoir Parameters
		# To quickly test that the code works, try 4 atoms.
		# To confirm our results, the hyperparameters are listed in the appendix  of our pdf document
		self.nb_atoms = 9

		self.inp_duration = 1000
		self.N_samples = 1024
		self.reset_rate = 0.
		self.geometry = "grid_lattice_centred"
		self.atom_distance = 15

		# For Hyperparameter search
		# Classical
		self.nb_neurons_list = [
			4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 30, 35, 40, 50, 60, 70, 80, 90, 100]
		# Quantum
		self.sample_len_list = [2, 3, 6, 8, 9, 10]
		self.nb_atoms_list = [9]
		self.inp_duration_list = [16, 100, 1000]
		self.N_samples_list = [1024]
		self.reset_rate_list = [0.]
		self.geometry_list = ["grid_lattice_centred"]
		self.atom_distance_list = [4, 8, 11, 13, 14, 15, 20, 35]
		# Potentially usable for both the classical & quantum hyperparameter searches
		# Warning ! It is not recommended to change such parameters for the quantum hyp. search by default,
		# in order not to make a default search too long
		self.input_type_list = ["sine"]
		self.train_len_list = [self.train_len]
		self.test_len_list = [self.test_len]

		self.real_train_len = self.train_len - self.sample_len
		self.real_test_len = self.test_len - self.sample_len

		# Energy comparisons
		self.dataset_sizes = [1000 * i for i in range(1, 10 ** 4 + 1)]
		self.S = 10
		self.T_pulse = 1e-6
		self.N_runs = 52

data = Dataset()
