# Generated by Django 4.2 on 2023-06-08 22:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import embed_video.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Conteudo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=100, unique=True)),
                ("imagem", models.ImageField(upload_to="imagems/")),
                ("sinopse", models.TextField()),
                ("url", embed_video.fields.EmbedVideoField(blank=True)),
                ("elenco", models.CharField(max_length=100)),
                ("criado_em", models.DateTimeField(auto_now_add=True)),
                (
                    "idade_recomendada",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(10),
                            django.core.validators.MaxValueValidator(18),
                        ]
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Bem Avaliado", "Bem Avaliado"),
                            ("Normal", "Normal"),
                        ],
                        default="Normal",
                        max_length=12,
                    ),
                ),
                (
                    "genero",
                    models.CharField(
                        choices=[("Filme", "Filme"), ("Serie", "Serie")], max_length=5
                    ),
                ),
                (
                    "genero_cinematografico",
                    models.CharField(
                        choices=[
                            ("Acao", "Acao"),
                            ("Aventura", "Aventura"),
                            ("Comedia", "Comedia"),
                            ("Documentario", "Documentario"),
                            ("Drama", "Drama"),
                            ("Fantasia", "Fantasia"),
                            ("Musical", "Musical"),
                            ("Terror", "Terror"),
                            ("Romance", "Romance"),
                            ("Ficcao", "Ficcao"),
                        ],
                        max_length=12,
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="like_post",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "salvo",
                    models.ManyToManyField(
                        blank=True,
                        related_name="salvar_post",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-criado_em"],
            },
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "conteudo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="conteudo.conteudo",
                    ),
                ),
                (
                    "usuario",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
