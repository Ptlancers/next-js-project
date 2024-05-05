// // Prevents additional console window on Windows in release, DO NOT REMOVE!!
// #![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]
// use tauri::Window;
// use std::process::Command;

// fn main() {
//     tauri::Builder::default()
//         .run(tauri::generate_context!())
//         .expect("error while running tauri application");
//         start_fastapi()
// }

// #[tauri::command]
// async fn start_fastapi(window: Window) -> Result<(), String> {
//     let command_result = Command::new("C:/Users/Administrator/Desktop/Projects/next-js-project/api/dist/index.exe").spawn();
//     if let Err(err) = command_result {
//         return Err(format!("Error executing Command {}", err));
//     }
    
//     // Show the window
//     if let Err(err) = window.show() {
//         return Err(format!("Error showing window: {}", err));
//     }
    
//     Ok(())
// }

#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use std::process::Command;
use tauri::Window;

fn main() {
    tauri::Builder::default()
        .run(tauri::generate_context!())
        .expect("error while running tauri application");

    // Call the start_fastapi function after Tauri has been initialized
    start_fastapi();
}

#[tauri::command]
async fn start_fastapi() -> Result<(), String> {
    let command_result = Command::new("C:/Users/Administrator/Desktop/Projects/next-js-project/api/dist/index.exe").spawn();
    if let Err(err) = command_result {
        println!("{}",format!("Error executing Command {}", err));
    }
    Ok(())
}
