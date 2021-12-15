import java.io.*;
import java.util.*;
public class Book {
   
    private int bookID;           // ID given by a library to a book to make it distinguishable from other books
    private String title;         // Title of a book 
    private String subject;       // Subject to which a book is related!
    private String author;        // Author of book!
    private boolean isIssued;        // this will be true if the book is currently issued to some borrower.