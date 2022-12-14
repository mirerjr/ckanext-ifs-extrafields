# encoding: utf-8
from __future__ import annotations

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class IfsExtrafieldsPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IDatasetForm)
    plugins.implements(plugins.IConfigurer)    
    
    def create_package_schema(self):
        schema = super(IfsExtrafieldsPlugin, self).create_package_schema()
        
        schema.update({
            # Área do conhecimento: conforme a tabela do CNPq
            'area_conhecimento': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            
            # Campus: Nome do campus onde foi realizada a PPI 
            'campus': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # Curso: Nome do curso onde foi desenvolvida a PPI 
            'curso': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # Tipo de componente: Atividade Complementar ou Componente Curricular conforme cadastro no SIGAA e informação no PPC. 
            'tipo_componente': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # Período/ano: Especificar se é 1º, 2º, ou 3º ano 
            'periodo_ano': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # Carga horária: Quantidade de horas empregadas no desenvolvimento da PPI. 
            'carga_horaria': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # Disciplinas: Nomes dos componentes curriculares de base comum e/ou de formação profissional envolvidos no desenvolvimento da PPI. 
            'disciplinas': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # APL: Conforme os indicados em https://www.gov.br/empresas-enegocios/pt-br/observatorioapl/nucleos-estaduais/sergipe 
            'apl': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # Área do conhecimento: conforme a tabela do CNPq.
            'area_conhecimento': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],

            # Fator de Inovação: taxonomia desenvolvida pela equipe gestora do OBEMI-IFS - ver em anexos.        
            'fator_inovacao': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
        })

        return schema

    def update_package_schema(self):
        schema = super(IfsExtrafieldsPlugin, self).update_package_schema()
        
        schema.update({
            'area_conhecimento': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'campus': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'curso': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'tipo_componente': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'periodo_ano': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'carga_horaria': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'disciplinas': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'apl': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'area_conhecimento': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
            'fator_inovacao': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_to_extras')],
        })

        return schema

    def show_package_schema(self):
        schema = super(IfsExtrafieldsPlugin, self).show_package_schema()
        
        schema.update({
            'area_conhecimento': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'campus': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'curso': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'tipo_componente': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'periodo_ano': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'carga_horaria': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'disciplinas': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'apl': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'area_conhecimento': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
            'fator_inovacao': [toolkit.get_validator('ignore_missing'), toolkit.get_converter('convert_from_extras')],
        })

        return schema

    def is_fallback(self):
        # Retorna True para registrar este plugin como o principal gerenciador dos tipos
        # de dataset que não são gerenciados por nenhum outro plugin IDatasetForm
        return True

    def package_types(self):
        # Este plugin não gerencia nenhum tipo específico de dataset,
        # ele apenas se registra como a escolha padrão (is_fallback)
        return []

    def update_config(self, config):
        # Adiciona o diretório do template deste plugin para o 'extra_template_paths do CKAN,
        # Com isso o CKAN vai utilizar o template customziado deste plugin
        toolkit.add_template_directory(config, 'templates')