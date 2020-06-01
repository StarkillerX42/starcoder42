import unittest
from python import starcoder42 as s
import numpy as np
import matplotlib.pyplot as plt


class NBodySimulation(unittest.TestCase):
    def test_force(self):
        force = s.force_gravity(s.m_earth, s.m_sun,
                        [0, 0, 1*s.distances['AstronomicalUnits']], [0, 0., 0.]
        )
        self.assertIsInstance(force, np.ndarray)
        self. assertTrue(all(force/1e23 < 1))
        print(force)

    def test_nbody_plot(self):
        # masses = np.random.random(3) * (s.m_earth + s.m_sun) / 2.
        # ipositions = np.random.random((3, 3)) * s.distances['AstronomicalUnits']
        # ivelocities = np.random.random((3, 3)) * 20000  # km/s of Earth
        # t = 500. * s.times['Days']
        # dt = t / 1000.
        masses = [s.m_earth, 70]
        ipositions = [[0, 0, 0], [0, s.distances['EarthRadii'], 0]]
        ivelocities = [[0, 0, 0], [25, 25, 0]]
        t = 2
        dt = 0.1
        positions, velocities, times = s.calculate_trajectories(
            masses, ipositions, ivelocities, t, dt, s.force_gravity
        )
        print(positions)
        fig = plt.figure(figsize=(6, 4))
        ax = fig.gca()
        ax.scatter(positions[:, 1, 0], positions[:, 1, 1])
        ax.quiver(positions[:, 1, 0], positions[:, 1, 1],
                      velocities[:, 1, 0], velocities[:, 1, 1])

        fig.savefig('nbody_test.png')
        self.assertTrue(True)

    def test_energy(self):
        masses = np.random.random(3) * (s.m_earth + s.m_sun) / 2.
        ipositions = np.random.random((3, 3)) * s.distances['AstronomicalUnits']
        ivelocities = np.random.random((3, 3)) * 30000  # km/s of Earth
        t = 500. * s.times['Days']
        dt = t/1000.
        positions, velocities, times = s.calculate_trajectories(
            masses, ipositions, ivelocities, t, dt, s.force_gravity
        )
        u_tot = []
        for i, time in enumerate(times):
            u_tot.append(s.calculate_energy(masses, positions[i], velocities[i])
                         )
        u_tot = np.array(u_tot)
        delta_u = np.diff(u_tot)
        print('Here is the change in energy over time')
        s.describe(delta_u)


if __name__ == '__main__':
    unittest.main()
