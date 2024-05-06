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
## CycleGAN
Le CycleGAN est un modèle de réseau génératif utilisé pour apprendre la correspondance entre deux ensembles de données sans correspondance directe. 

Dans ce contexte, nous utilisons le CycleGAN pour apprendre la transformation entre les images générées par les GAN spécialisés et les versions altérées de ces images.

## Architecture

```mermaid
   graph TD;
   START("GAN Spécialisé") --> A
   A --> B("Altération")
   B --> C("GAN Spécialisé Altéré")

   style START fill:#FFFFFF00, stroke:#FFFFFF00;
```

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
![image](https://github.com/Dedhal/IA_GAN_NLP/assets/130046017/be787993-83bf-4d12-9087-5b8b00892892)
Dans l'architecture présentée, nous avons deux parties principales :

1. **GAN Spécialisé** : Il s'agit d'un modèle de réseau génératif spécialisé conçu pour générer des images dans un domaine spécifique. Par exemple, dans le contexte des images de chevaux, le GAN spécialisé apprendrait à générer des images réalistes de chevaux. Ces images peuvent être créées à partir de zéro ou être une transformation de données d'entrée, selon la conception du GAN.

2. **Altération avec CycleGAN** : Cette partie utilise le modèle CycleGAN pour altérer les images générées par les GAN spécialisés. Le CycleGAN est un type de réseau génératif adversaire qui apprend à transformer des images d'un domaine source en images d'un domaine cible, sans nécessiter de correspondance directe entre les paires d'images dans les deux domaines. Dans notre cas, les images générées par les GAN spécialisés servent de domaine source, tandis que les images altérées constituent le domaine cible.

L'ensemble du processus fonctionne de la manière suivante :

- Les images générées par les GAN spécialisés sont envoyées à l'étape d'altération avec le CycleGAN.
- Le CycleGAN utilise son modèle entraîné pour transformer ces images selon le style ou les caractéristiques souhaités. Par exemple, il peut altérer les images de chevaux pour qu'elles ressemblent davantage à des zèbres, ou pour ajouter des caractéristiques artistiques spécifiques.
- Les images altérées peuvent ensuite être utilisées comme sortie finale, ou être soumises à d'autres traitements, comme la classification ou d'autres formes de transformation d'image.

Cette architecture permet de créer un processus en boucle où les GAN spécialisés génèrent des images de départ, qui sont ensuite transformées par le CycleGAN pour produire une variété d'images altérées. Cela permet d'augmenter la diversité et la qualité des données générées, ainsi que d'explorer différentes variations de styles ou de caractéristiques dans les images finales.
