import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.rahallinen_maksukortti = Maksukortti(10000)
        self.tyhja_maksukortti = Maksukortti(0)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_luodun_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_luodun_kassapaatteen_myydyt_edulliset_maara_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_luodun_kassapaatteen_myydyt_maukkaat_maara_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateisosto_toimii_jos_rahaa_riittaa(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(vaihtoraha, 10)

    def test_edullinen_kateisosto_palauttaa_oikein_jos_rahamaara_vaarin(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vaihtoraha, 230)

    def test_maukas_kateisosto_toimii_jos_raha_riittaa(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(vaihtoraha, 100)

    def test_maukas_kateisosto_palauttaa_oikein_jos_rahamaara_vaarin(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(230)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vaihtoraha, 230)

    def test_edullinen_korttiosto_toimii_jos_raha_riittaa(self):
        veloita = self.kassapaate.syo_edullisesti_kortilla(self.rahallinen_maksukortti)
        self.assertEqual(veloita, True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_korttiosto_palauttaa_oikein_jos_kortti_tyhja(self):
        veloita = self.kassapaate.syo_edullisesti_kortilla(self.tyhja_maksukortti)
        self.assertEqual(veloita, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_korttiosto_toimii_jos_raha_riittaa(self):
        veloita = self.kassapaate.syo_maukkaasti_kortilla(self.rahallinen_maksukortti)
        self.assertEqual(veloita, True)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_korttiosto_palauttaa_oikein_jos_kortti_tyhja(self):
        veloita = self.kassapaate.syo_maukkaasti_kortilla(self.tyhja_maksukortti)
        self.assertEqual(veloita, False)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_lataus_positiivinen_maara_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.tyhja_maksukortti, 5)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100005)

    def test_negatiivinen_maara_kortin_lataaminen_ei_nosta_kateiskassaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.tyhja_maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)