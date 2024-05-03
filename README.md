# IA_GAN_NLP

## Goal:
Le but de ce projet est de réussir a créer un modèle prennant une description textuelle en entrée pour générer une image de sortie.
Dans le but d'obtenir les sorties les plus cohérentes possibles, nous créerons plusieurs GAN chacun spécialisé dans la création d'une classe d'image.
Une modèle de Transformer s'occupera de la classification pour choisir le GAN a appeler.

En fonction du temps nécessaire pour les entraînements, nous tenterons plusieurs modèles, en particulier sur les GAN.
Nous pourrons aussi, si le temps nous le permet augmenter l'architecture avec une couche d'altération.

## Structure


### Structure Simple

```mermaid
   graph TD;
   A("Transformer Classifier")-->B("GAN Spécialisé");
   A-->C("GAN Spécialisé");
   A-->D("GAN Spécialisé");
   A-->E("...");
   B-->F("Output");
   C-->F;
   D-->F;
   E-->F;
```

### Avec Altération

```mermaid
   graph TD;
   A("Transformer Classifier")-->B("GAN Spécialisé");
   A-->C("GAN Spécialisé");
   A-->D("GAN Spécialisé");
   A-->E("...");
   A-->F("Altération<br>Cycle GAN");
   B-->F;
   C-->H("Altération<br>Cycle GAN");
   A-->H;
   D-->I("Altération<br>Cycle GAN");
   A-->I;
   E-->J("...");
   A-->J;
   F-->G("Output");
   H-->G;
   I-->G;
   J-->G;
   
```
