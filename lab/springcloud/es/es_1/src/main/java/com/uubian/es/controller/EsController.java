package com.uubian.es.controller;


import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.elasticsearch.core.ElasticsearchTemplate;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.uubian.es.domain.elasticsearch.Article;
import com.uubian.es.repository.elasticsearch.ArticleRepository;



@RestController()
@RequestMapping("/es")
public class EsController {
	@Autowired
	private ArticleRepository articleRepository;
	@Autowired
	private ElasticsearchTemplate template;
	
	@GetMapping("/test")
	public Article getAll(){
		//template.createIndex(Article.class);
		
		Article article= new Article();
		article.setTitle("纪念刘和珍君");
		article.setContent("一个名叫纪念刘和珍君的文章的内容");
		return articleRepository.save(article);
	}
	@GetMapping("/query/{title}")
	public List<Article> Query(@PathVariable String title){
		//template.createIndex(Article.class);
		
		return articleRepository.findByTitle(title);
	}
	
}
