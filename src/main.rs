use eframe::egui;

fn main() -> eframe::Result {
    let options = eframe::NativeOptions::default();
    eframe::run_native(
        "conway.desktop",
        options,
        Box::new(|cc| Ok(Box::new(ConwayApp::new(cc)))),
    )
}

// enum CellState {
//     Dead,
//     Alive,
// }

#[derive(Default)]
struct ConwayApp {
    grid: Vec<Vec<bool>>,
}

impl ConwayApp {
    fn new(cc: &eframe::CreationContext<'_>) -> Self {
        let width = 50;
        let height = 50;

        let grid = vec![vec![false; width]; height];
        // grid[10][10] = true;
        // grid[1][12] = true;
        // grid[11][13] = true;

        Self { grid }
    }
}

impl eframe::App for ConwayApp {
    fn ui(&mut self, ui: &mut egui::Ui, frame: &mut eframe::Frame) {
        // Défini le style de la fenêtre vide, "sans ses composants"
        let custom_frame = egui::containers::Frame {
            fill: egui::Color32::LIGHT_GRAY,
            ..Default::default()
        };

        // Défini une fenêtre "CentralPanel" qui prend tout l'espace disponible (par définition)...
        egui::CentralPanel::default()
            .frame(custom_frame)
            .show_inside(ui, |ui| {
                let cell_size = 20.0;

                let (response, painter) =
                    ui.allocate_painter(ui.available_size(), egui::Sense::hover());

                let frame = response.rect;

                // ...dans laquelle on introduit des subdivisions horizontales centrée "horizontal" (par définition)...
                for y in 0..self.grid.len() {
                    ui.horizontal(|ui| {
                        // ...dans lesquelles on introduit des canvas qui correspondent aux cellules avec le comportement souhaité
                        for x in 0..self.grid[y].len() {
                            let position = egui::pos2(
                                frame.left() + x as f32 * cell_size,
                                frame.top() + y as f32 * cell_size,
                            );

                            let cell = egui::Rect::from_min_size(
                                position,
                                egui::vec2(cell_size, cell_size),
                            );

                            let alive = self.grid[y][x];

                            let color = if alive {
                                egui::Color32::DARK_GRAY
                            } else {
                                egui::Color32::WHITE
                            };

                            painter.rect_filled(cell, 0.0, color);
                            painter.rect_stroke(
                                cell,
                                0.0,
                                egui::Stroke::new(1.0, egui::Color32::LIGHT_GRAY),
                                egui::StrokeKind::Middle,
                            );
                        }
                    });
                }
            });
    }
}
