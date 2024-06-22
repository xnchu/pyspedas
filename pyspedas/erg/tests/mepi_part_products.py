
import os
import unittest
from pytplot import data_exists, del_data, timespan,tplot
from pyspedas.erg import erg_mep_part_products

import pyspedas
import pytplot

display=False

class LoadTestCases(unittest.TestCase):

    def test_mepi_theta(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        # Calculate and plot energy spectrum
        vars = erg_mep_part_products( 'erg_mepi_l2_3dflux_FPDU', outputs='theta', trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'] )
        tplot( 'erg_mepi_l2_3dflux_FPDU_theta', display=display, save_png='erg_mepi_theta.png' )

    def test_mepi_phi(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        # Calculate and plot energy spectrum
        vars = erg_mep_part_products( 'erg_mepi_l2_3dflux_FPDU', outputs='phi', trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'] )
        tplot( 'erg_mepi_l2_3dflux_FPDU_phi', display=display, save_png='erg_mepi_phi.png' )


    def test_mepi_pa(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        vars = pyspedas.erg.mgf(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary B-field data
        vars = pyspedas.erg.orb(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary orbit data
        mag_vn = 'erg_mgf_l2_mag_8sec_dsi'
        pos_vn = 'erg_orb_l2_pos_gse'

        # Calculate and plot energy spectrum
        vars = erg_mep_part_products( 'erg_mepi_l2_3dflux_FPDU', mag_name=mag_vn, pos_name=pos_vn, outputs='pa', trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'] )
        tplot( 'erg_mepi_l2_3dflux_FPDU_pa', display=display, save_png='erg_mepi_pa.png' )

    def test_mepi_moments(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        vars = pyspedas.erg.mgf(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary B-field data
        vars = pyspedas.erg.orb(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary orbit data
        mag_vn = 'erg_mgf_l2_mag_8sec_dsi'
        pos_vn = 'erg_orb_l2_pos_gse'

        # Calculate and plot energy spectrum
        vars = erg_mep_part_products( 'erg_mepi_l2_3dflux_FPDU', mag_name=mag_vn, pos_name=pos_vn, outputs='moments', trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'] )
        print(vars)
        tplot(vars, display=display, save_png='erg_mepi_moments.png' )

    def test_mepi_fac_moments(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        vars = pyspedas.erg.mgf(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary B-field data
        vars = pyspedas.erg.orb(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary orbit data
        mag_vn = 'erg_mgf_l2_mag_8sec_dsi'
        pos_vn = 'erg_orb_l2_pos_gse'

        # Calculate and plot energy spectrum
        vars = erg_mep_part_products( 'erg_mepi_l2_3dflux_FPDU', mag_name=mag_vn, pos_name=pos_vn, outputs='fac_moments', trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'] )
        print(vars)
        tplot(vars, display=display, save_png='erg_mepi_fac_moments.png' )

    def test_mepi_fac_energy(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        vars = pyspedas.erg.mgf(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary B-field data
        vars = pyspedas.erg.orb(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary orbit data
        mag_vn = 'erg_mgf_l2_mag_8sec_dsi'
        pos_vn = 'erg_orb_l2_pos_gse'

        # Calculate and plot energy spectrum
        vars = erg_mep_part_products( 'erg_mepi_l2_3dflux_FPDU', mag_name=mag_vn, pos_name=pos_vn, outputs='fac_energy', trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'] )
        print(vars)
        tplot(vars, display=display, save_png='erg_mepi_fac_energy.png' )

    def test_mepi_en_spec(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        # Calculate and plot energy spectrum
        vars = erg_mep_part_products( 'erg_mepi_l2_3dflux_FPDU', outputs='energy', trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'] )
        tplot( 'erg_mepi_l2_3dflux_FPDU_energy', display=display, save_png='erg_mepi_en_spec.png' )

    def test_mepi_pad(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        vars = pyspedas.erg.mgf(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary B-field data
        vars = pyspedas.erg.orb(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary orbit data
        mag_vn = 'erg_mgf_l2_mag_8sec_dsi'
        pos_vn = 'erg_orb_l2_pos_gse'
        # Calculate the pitch angle distribution
        vars = erg_mep_part_products('erg_mepi_l2_3dflux_FPDU', outputs='pa', energy=[15000., 22000.], fac_type='xdsi',
                                     mag_name=mag_vn, pos_name=pos_vn,
                                     trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])

        tplot( 'erg_mepi_l2_3dflux_FPDU_pa', display=display, save_png='erg_mepi_pad.png' )

    def test_mepi_en_pad_limit(self):
        del_data('*')
        # Load MEP-i Lv.2 3-D flux data
        timespan('2017-04-05 21:45:00', 2.25, keyword='hours')
        pyspedas.erg.mepi_nml( trange=[ '2017-04-05 21:45:00', '2017-04-05 23:59:59'], datatype='3dflux' )
        vars = pyspedas.erg.mgf(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary B-field data
        vars = pyspedas.erg.orb(trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'])  # Load necessary orbit data
        mag_vn = 'erg_mgf_l2_mag_8sec_dsi'
        pos_vn = 'erg_orb_l2_pos_gse'
        # Calculate energy-time spectra of electron flux for limited pitch-angle (PA) ranges
        ## Here we calculate energy-time spectra for PA = 0-10 deg and PA = 80-100 deg.
        vars = erg_mep_part_products('erg_mepi_l2_3dflux_FPDU', outputs='fac_energy', pitch=[80., 100.],
                                     fac_type='xdsi', mag_name=mag_vn, pos_name=pos_vn,
                                     trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'], suffix='_pa80-100')
        vars = erg_mep_part_products('erg_mepi_l2_3dflux_FPDU', outputs='fac_energy', pitch=[0., 10.], fac_type='xdsi',
                                     mag_name=mag_vn, pos_name=pos_vn,
                                     trange=['2017-04-05 21:45:00', '2017-04-05 23:59:59'], suffix='_pa0-10')

        ## Decorate the obtained spectrum variables
        pytplot.options('erg_mepi_l2_3dflux_FPDU_energy_mag_pa80-100', 'ytitle', 'MEP-i flux\nPA: 80-100\n\n[eV]')
        pytplot.options('erg_mepi_l2_3dflux_FPDU_energy_mag_pa0-10', 'ytitle', 'MEP-i flux\nPA: 0-10\n\n[eV]')
        tplot(['erg_mepi_l2_3dflux_FPDU_energy_mag_pa80-100', 'erg_mepi_l2_3dflux_FPDU_energy_mag_pa0-10'], display=display, save_png='erg_mep_en_pa_limit.png')

if __name__ == '__main__':
    unittest.main()