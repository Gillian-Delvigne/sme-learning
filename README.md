# sme-learning

**English** · [Français](#fr)

An adaptive learning engine for small and mid-sized companies. It **derives** a training
path instead of having someone author one.

## What it decides

Given an employee and the role they hold, the engine answers three questions:

1. **What is missing** — the skills the role requires, minus the skills the employee already has.
2. **What supplies it** — the courses that teach exactly those skills.
3. **In what order** — courses declare prerequisites, so a path is a topological order over
   a graph, not a list.

Then it asks all three again whenever a certification expires.

## The decision everything rests on

**Skills are the pivot, not courses.** `Skill` is linked three ways — to `Employee` (what
they have), to `Role` (what the job requires), to `Course` (what a course teaches).

Attaching courses directly to roles would have been simpler to write and would have lost
two things: you could no longer say *why* a course is prescribed, and a skill acquired
somewhere else — another job, a side project — could never be credited. The pivot keeps the
reason in the data.

## What wasn't trivial

- **Prerequisites are a graph, not an order.** `course_prerequisite` is a self-join on
  courses. Producing a path means a topological sort, and a cycle authored by mistake has to
  be rejected rather than looped over.
- **Expiry reopens a closed need.** `EnrollmentStatus` runs `ENROLLED → IN_PROGRESS →
  COMPLETED → CERTIFIED → EXPIRED`, and `certification_date` carries the clock. A finished
  path becomes a gap again, so prescription cannot be a one-off computation.
- **The pass rule lives in the data.** `Activity.pass_threshold` is a column, not a constant.
  Whoever writes a course changes the bar without a deployment.
- **One enrollment per employee and course** — `UniqueConstraint("employee_id",
  "course_id")`. Re-prescribing has to update a row, never insert a second one.

## The model

| | |
|---|---|
| `Employee` | holds a `Role`, accumulates `Skill`s, has `Enrollment`s |
| `Role` | requires `Skill`s |
| `Course` | teaches `Skill`s, declares prerequisites on other courses |
| `Activity` | ordered by `sequence`, typed `Quizz / Media / Text`, carries `pass_threshold` |
| `Enrollment` | the employee-course pair and its lifecycle |

## Modelled before it was coded

`docs/mcd/` holds the Merise conceptual and logical models and the generated DDL. The
schema was drawn, then written.

## Running it

```bash
pip install -r requirements.txt
cp .env.example .env     # DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
python seed.py
```

---

<a id="fr"></a>

## sme-learning — en français

[English](#sme-learning) · **Français**

Un moteur d'apprentissage adaptatif pour les PME. Il **calcule** un parcours de formation
au lieu de le faire rédiger.

### Ce qu'il décide

Pour un employé et le poste qu'il occupe, le moteur répond à trois questions :

1. **Ce qui manque** — les compétences exigées par le poste, moins celles que l'employé a déjà.
2. **Ce qui le comble** — les cours qui enseignent précisément ces compétences.
3. **Dans quel ordre** — les cours déclarent des prérequis : un parcours est donc un tri
   topologique sur un graphe, pas une liste.

Puis il repose les trois dès qu'une certification expire.

### La décision porteuse du projet

**Le pivot, ce sont les compétences, pas les cours.** `Skill` est lié trois fois — à
`Employee` (ce qu'il possède), à `Role` (ce que le poste exige), à `Course` (ce qu'un cours
enseigne).

Rattacher les cours directement aux postes aurait été plus simple à écrire, et aurait perdu
deux choses : on ne pouvait plus dire *pourquoi* un cours est prescrit, et une compétence
acquise ailleurs — un autre poste, un projet personnel — n'était jamais créditée. Le pivot
garde la raison dans les données.

### Ce qui n'était pas trivial

- **Les prérequis forment un graphe, pas un ordre.** `course_prerequisite` est un auto-lien
  sur les cours. Produire un parcours demande un tri topologique, et un cycle saisi par
  erreur doit être rejeté plutôt que parcouru.
- **L'expiration rouvre un besoin clos.** `EnrollmentStatus` va de `ENROLLED` à `EXPIRED`,
  et `certification_date` porte l'horloge. Un parcours terminé redevient un manque : la
  prescription ne peut donc pas être un calcul unique.
- **La règle de réussite vit dans les données.** `Activity.pass_threshold` est une colonne,
  pas une constante. Celui qui écrit un cours déplace la barre sans déploiement.
- **Une inscription par couple employé-cours** — `UniqueConstraint`. Re-prescrire doit
  mettre à jour une ligne, jamais en insérer une seconde.

### Modélisé avant d'être codé

`docs/mcd/` contient le MCD et le MLD Merise ainsi que le DDL généré. Le schéma a été
dessiné (MOCODO), puis écrit.
