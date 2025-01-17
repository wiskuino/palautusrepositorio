import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 3)
        self.juusto = Tuote("Oltermanni", 4)
        self.olut = Tuote("lava_porin_karhua",100)

    # step 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    # step 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_oikein(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), 3)

    #step 4
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
       self.kori.lisaa_tuote(self.maito)
       self.kori.lisaa_tuote(self.juusto)
       self.assertEqual(self.kori.tavaroita_korissa(), 2)

   # step 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_yhteishinta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.juusto)
        self.assertEqual(self.kori.hinta(), 7)
    
    # step 6
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        self.kori.lisaa_tuote(self.olut)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.kori.lisaa_tuote(self.olut)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    # step 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_on_yhteishinta(self):
        self.kori.lisaa_tuote(self.olut)
        self.kori.lisaa_tuote(self.olut)
        self.assertEqual(self.kori.hinta(), 200)

    # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
        # testaa että metodin palauttaman listan pituus 1

    #step 9 
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        self.kori.lisaa_tuote(self.maito)

        ostos = next(iter(self.kori.ostokset()))
        self.assertEqual(ostos, "Maito")
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        # testaa täällä, että palautetun listan ensimmäinen ostos on haluttu    
    
    #step 10
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_2_ostosta(self):
       self.kori.lisaa_tuote(self.maito)
       self.kori.lisaa_tuote(self.juusto)
       self.assertEqual(len(self.kori.ostokset()),  2)
       # testaa täällä, että palautetun listan pituus on 2 eli korissa on kaksi oliota

    #step 11
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_1_ostosta(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()),  1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()),  1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        # testaa täällä, että palautetun listan pituus on 2 eli korissa on yksi ostosolio, tavaroiden lukumäärä 2

    #step 12
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_1_ostosta_jolla_sama_nimi_kuin_tuotteella_ja_lukumäärä_2(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()),  1)
        self.assertEqual(next(iter(self.kori.ostokset())), "Maito")
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    #step 13
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_toinen_poistetaan_jää_koriin_ostos_ja_lukumäärä_1(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()),  1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(len(self.kori.ostokset()),  1)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    #step 14
    def test_tuotteen_lisaamisen_jalkeen_se_poistetaan_jolloin_kori_on_tyhjä_eli_korin_hinta_on_0_ja_listan_pituus_0(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.kori.poista_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(len(self.kori.ostokset()),  0)
        self.assertEqual(self.kori.hinta(), 0)

    #step 15
    def test_3_eri_tuotteen_lisaamisen_jalkeen_kori_tyhjennetään_jolloin_listan_pituus_0(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.juusto)
        self.kori.lisaa_tuote(self.olut)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.kori),  0)


