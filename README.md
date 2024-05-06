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


## ProGAN

Le ProGAN est un GAN que l'on fait progressivement grossir a chaque étape.

On commence par générer des images 4x4 avec un block de génération, puis, après un premier entrainement, on ajoute un block commençant par un Upsampling doublant la résolution, et un Layer d'interpolation.

Ce modèle a été utilisé pour générer des images de haute qualité.

[Publication de recherche](https://arxiv.org/pdf/1710.10196)

[source de l'implementation utilisée](https://github.com/DCtheTall/tf-keras-progressive-gan/blob/master/colab/progressive_gan.ipynb)

## Architecture

```mermaid
   graph TD;
   START("Bloc de Générateur") --> A

   style START fill:#FFFFFF00, stroke:#FFFFFF00;
```

```mermaid
   graph TD;
   START("Gen 1") -- Latent -->A("4x4 Generator")
   A-- 4x4 Generator Output -->B("4x4 Discriminator")
   STARTB("Gen 2")-- Latent -->C("4x4 Generator")
   C-->D("8x8 Generator")
   D-- 8x8 Generator Output --> E("8x8 Discriminator")
   E-->F("4x4 Discriminator")

   style START fill:#FFFFFF00, stroke:#FFFFFF00;
   style STARTB fill:#FFFFFF00, stroke:#FFFFFF00;
```
