from seleniumbase import BaseCase
import pygame
BaseCase.main(__name__, __file__)
import time

class MyTestClass(BaseCase):
    def test_swag_labs(self):
        self.open("https://cdn-statiques.phm.education.gouv.fr/exaco/cyclades/portailcandi/resources/cnx/publicationNotes.html")

        self.type('input#username', 'prenom.nom') #mettre identifiant
        self.type('input#password', 'mdp') #mettre mdp

        notes_publiees = False
        while not notes_publiees:

            self.click('input.bouton-acces[type="submit"]')

            if self.assert_text("Vos notes n\'ont pas encore été publiées, veuillez renouveler votre demande ultérieurement."):
                print("pas de note")
                time.sleep(2)
                self.go_back()
                time.sleep(600) #wait de 20 minutes si mes calculs sont bons
            else:
                notes_publiees = True
                print("test té")
                pygame.mixer.init()
                pygame.mixer.music.load("bac.wav")
                pygame.mixer.music.play()

                while pygame.mixer.music.get_busy():
                    time.sleep(1)
                    
        self.close()