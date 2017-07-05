package com.uubian.es.repository.elasticsearch;

import java.util.List;

import org.springframework.data.elasticsearch.repository.ElasticsearchRepository;
import org.springframework.stereotype.Repository;

import com.uubian.es.domain.elasticsearch.Article;

@Repository
public interface  ArticleRepository extends ElasticsearchRepository<Article, String> {
	public List<Article> findByTitle(String title);
}