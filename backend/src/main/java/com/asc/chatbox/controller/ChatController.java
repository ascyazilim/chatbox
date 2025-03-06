package com.asc.chatbox.controller;

import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.Map;

@RestController
@RequestMapping("/chat")
public class ChatController {

    private final String PYTHON_API_URL = "http://localhost:8000/chat";

    @PostMapping
    public ResponseEntity<Map<String, String>> chatWithModel(@RequestBody Map<String, String> requestBody) {
        RestTemplate restTemplate = new RestTemplate();
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<Map<String, String>> entity = new HttpEntity<>(requestBody, headers);

        ResponseEntity<Map> response = restTemplate.exchange(PYTHON_API_URL, HttpMethod.POST, entity, Map.class);
        Map<String, String> responseBody = new HashMap<>();
        responseBody.put("response", response.getBody().get("response").toString());

        return ResponseEntity.ok(responseBody);
    }
}
